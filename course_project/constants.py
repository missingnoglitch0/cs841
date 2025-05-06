# Run it!
cn_TIMESTAMP = 'Timestamp'
cn_TIME_REL_ANCHOR = 'Time Relative to Anchor Event'

cn_PUPIL_DIAM = 'Pupil Diameter'
cn_TRIAL_IDX = 'Trial Index'

# time columns
cn_TIME_BEG = 'Time Beg' # time at which trial begins
cn_TIME_BEHAVIOR = 'Time Behavior' # time at which behavior/action is taken
cn_TIME_REWARD = 'Time Reward' # time at which reward is shown/given/administered
cn_TIME_END = 'Time End' # time at which trial ends
# having all of these timestamps allows us to retrieve pupil samples for each trial individually

cn_SETUP_CHOICE_CORRECT = 'Setup Correct Choice'
cn_RESULT_CHOICE_USR = 'Choice by User'
cn_RESULT_CHOICE_PRG = 'Choice by Program'
cn_RESULT_CORRECTNESS = 'Correct'

cn_EXPERIMENTAL_EVENT = 'Experimental Event'
EXPERIMENTAL_EVENT_MISBEHAVIOR = 'Misbehavior'
EXPERIMENTAL_EVENT_RANDOM_SWITCH = 'Random Task Switch'

columns_events = [cn_TRIAL_IDX, cn_TIME_BEG, cn_TIME_BEHAVIOR, cn_TIME_REWARD, cn_TIME_END,
                  cn_RESULT_CHOICE_USR, cn_RESULT_CHOICE_PRG, cn_SETUP_CHOICE_CORRECT, cn_RESULT_CORRECTNESS, cn_EXPERIMENTAL_EVENT]