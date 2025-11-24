from youtube_transcript_api import YouTubeTranscriptApi

# Check what methods are actually available
print("Available methods:")
print(dir(YouTubeTranscriptApi))

# Check the type
print(f"\nType: {type(YouTubeTranscriptApi)}")

# Check the module it came from
print(f"\nModule: {YouTubeTranscriptApi.__module__}")