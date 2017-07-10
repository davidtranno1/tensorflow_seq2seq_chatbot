GENERATED_DIR = "/Users/higepon/Desktop/generated"
LOGS_DIR = "/Users/higepon/Desktop/train_logs"

is_fast_build = True
is_beam_search_enabled = True

DATA_DIR = "data"
if is_fast_build:
    TWEETS_TXT = "{0}/tweets_short.txt".format(DATA_DIR)
else:
    TWEETS_TXT = "{0}/tweets.txt".format(DATA_DIR)

if is_fast_build:
    MAX_ENC_VOCABULARY = 6
    NUM_LAYERS = 1
    LAYER_SIZE = 2
    BATCH_SIZE = 3
    buckets = [(4, 13), (8, 14)]
else:
    MAX_ENC_VOCABULARY = 50000
    NUM_LAYERS = 3
    LAYER_SIZE = 256 ## embed_size
    BATCH_SIZE = 64
    buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]

MAX_DEC_VOCABULARY = MAX_ENC_VOCABULARY

LEARNING_RATE = 0.5
LEARNING_RATE_DECAY_FACTOR = 0.99
MAX_GRADIENT_NORM = 5.0

TWEETS_TRAIN_ENC_IDX_TXT = "{0}/tweets_train_enc_idx.txt".format(GENERATED_DIR)
TWEETS_TRAIN_DEC_IDX_TXT = "{0}/tweets_train_dec_idx.txt".format(GENERATED_DIR)
TWEETS_VAL_ENC_IDX_TXT = "{0}/tweets_val_enc_idx.txt".format(GENERATED_DIR)
TWEETS_VAL_DEC_IDX_TXT = "{0}/tweets_val_dec_idx.txt".format(GENERATED_DIR)

VOCAB_ENC_TXT = "{0}/vocab_enc.txt".format(GENERATED_DIR)
VOCAB_DEC_TXT = "{0}/vocab_dec.txt".format(GENERATED_DIR)
