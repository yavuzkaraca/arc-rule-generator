try
    % Basic PTB setup
    PsychDefaultSetup(2);
    Screen('Preference', 'SkipSyncTests', 1); % remove in real experiments
    screenNumber = max(Screen('Screens'));
    white = WhiteIndex(screenNumber);
    black = BlackIndex(screenNumber);

    [win, winRect] = PsychImaging('OpenWindow', screenNumber, black);
    [xCenter, yCenter] = RectCenter(winRect);

    % Initialize EyeLink connection
    if ~EyelinkInit()
        error('EyeLink Init failed');
    end

    % Create defaults structure for calibration etc.
    el = EyelinkInitDefaults(win);

    % Optional visual customization of calibration target
    el.backgroundcolour = black;
    el.foregroundcolour = white;
    el.targetbeep = 1;
    el.feedbackbeep = 1;
    EyelinkUpdateDefaults(el);

    % Open EDF file on tracker PC
    edfFile = 'demo.edf';
    Eyelink('OpenFile', edfFile);

    % Tell tracker what data to save / stream
    Eyelink('Command', 'file_sample_data = LEFT,RIGHT,GAZE,AREA,STATUS');
    Eyelink('Command', 'link_sample_data = LEFT,RIGHT,GAZE,AREA,STATUS');

    % Calibration / validation
    EyelinkDoTrackerSetup(el);

    % Optional drift correction before a block
    EyelinkDoDriftCorrection(el);

    % Start recording
    Eyelink('StartRecording');
    WaitSecs(0.1);

    % Mark trial start in EDF
    Eyelink('Message', 'TRIALID 1');

    trialDur = 2.0;
    tStart = GetSecs;

    while GetSecs - tStart < trialDur
        % Draw fixation
        Screen('FillOval', win, white, CenterRectOnPoint([0 0 12 12], xCenter, yCenter));
        Screen('Flip', win);

        % Online gaze access
        if Eyelink('NewFloatSampleAvailable') > 0
            evt = Eyelink('NewestFloatSample');
            eyeUsed = Eyelink('EyeAvailable');
            if eyeUsed == el.BINOCULAR
                eyeUsed = el.LEFT_EYE;
            end

            gx = evt.gx(eyeUsed + 1);
            gy = evt.gy(eyeUsed + 1);
            pa = evt.pa(eyeUsed + 1);

            % gx, gy are current gaze coordinates
            % pa is pupil area
            if pa > 0
                % Example: do something with gaze
            end
        end
    end

    % Mark trial end
    Eyelink('Message', 'TRIAL_RESULT 0');

    % Stop recording
    Eyelink('StopRecording');

    % Close EDF on tracker and transfer to stimulus PC
    Eyelink('CloseFile');
    Eyelink('ReceiveFile', edfFile, pwd, 1);

    % Shutdown
    Eyelink('Shutdown');
    sca;

catch ME
    Eyelink('Shutdown');
    sca;
    rethrow(ME);
end