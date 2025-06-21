from main import speakers
from schemas.speaker import SpeakerCreate, Speaker

def get_all_speakers():
    return speakers

def get_speaker_by_id(speaker_id: int):
    return next((s for s in speakers if s.id == speaker_id), None)

def create_speaker(speaker_data: SpeakerCreate):
    new_id = len(speakers) + 1
    speaker = Speaker(
        id=new_id,
        name=speaker_data.name,
        topic=speaker_data.topic
    )
    speakers.append(speaker)
    return speaker

def update_speaker(speaker_id: int, speaker_data: SpeakerCreate):
    speaker = get_speaker_by_id(speaker_id)
    if speaker:
        speaker.name = speaker_data.name
        speaker.topic = speaker_data.topic
        return speaker
    return None

def delete_speaker(speaker_id: int):
    speaker = get_speaker_by_id(speaker_id)
    if speaker:
        speakers.remove(speaker)
        return True
    return False
