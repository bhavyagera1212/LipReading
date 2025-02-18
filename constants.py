# TOTAL_FRAMES = 25
# VALID_WORD_THRESHOLD = 1
# NOT_TALKING_THRESHOLD = 10
# PAST_BUFFER_SIZE = 4
# LIP_WIDTH = 112
# LIP_HEIGHT = 80

# Constants for capturing and processing
TOTAL_FRAMES = 30  # Reduce to ensure each word captures concise and relevant frames.
VALID_WORD_THRESHOLD = 10  # Adjusted to allow shorter word sequences if necessary.
NOT_TALKING_THRESHOLD = 5  # Lowered to reduce the time before the system identifies the end of a word.
PAST_BUFFER_SIZE = 5  # Increase to include more pre-word frames, which may help with alignment.
LIP_WIDTH = 112  # No change, as this is likely standard for input resolution.
LIP_HEIGHT = 80  # No change, aligned with typical input dimensions for ML models.

