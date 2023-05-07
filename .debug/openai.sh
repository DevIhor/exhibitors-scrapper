# list engines
openai api engines.list

# Generate image with DALL-E
openai api image.create -p <some-text> -n 1

# create a completion
openai api completions.create -e ada -p <some-text>