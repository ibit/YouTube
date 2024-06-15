from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
import re

def get_video_id(url):
    # 正規表現を使ってYouTubeの動画IDを抽出
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("有効なYouTube動画のURLを入力してください")

def get_transcript_from_url(url):
    try:
        video_id = get_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except NoTranscriptFound:
        return "この動画には字幕がありません。"
    except TranscriptsDisabled:
        return "この動画の字幕は無効になっています。"
    except VideoUnavailable:
        return "この動画は利用できません。"
    except Exception as e:
        return str(e)

def main():
    # YouTube動画のURLを指定
    url = input("YouTube動画のURLを入力してください: ")

    # 字幕を取得
    transcript = get_transcript_from_url(url)

    # 字幕を表示
    if isinstance(transcript, list):
        for entry in transcript:
            print(f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}")
    else:
        print(f"エラーが発生しました: {transcript}")

if __name__ == "__main__":
    main()
