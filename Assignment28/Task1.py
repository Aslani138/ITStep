from abc import ABC, abstractmethod

# Interface for basic play functionality
class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

# Interface for pause functionality
class Pausable(ABC):
    @abstractmethod
    def pause(self):
        pass

# Interface for stop functionality
class Stoppable(ABC):
    @abstractmethod
    def stop(self):
        pass

# Interface for rewind functionality
class Rewindable(ABC):
    @abstractmethod
    def rewind(self):
        pass

# Interface for fast forward functionality
class FastForwardable(ABC):
    @abstractmethod
    def fast_forward(self):
        pass

# AudioPlayer implementing relevant interfaces
class AudioPlayer(Playable, Pausable, Stoppable):
    def play(self):
        print("Playing audio")

    def pause(self):
        print("Pausing audio")

    def stop(self):
        print("Stopping audio")

# VideoPlayer implementing relevant interfaces
class VideoPlayer(Playable, Pausable, Stoppable, Rewindable, FastForwardable):
    def play(self):
        print("Playing video")

    def pause(self):
        print("Pausing video")

    def stop(self):
        print("Stopping video")

    def rewind(self):
        print("Rewinding video")

    def fast_forward(self):
        print("Fast forwarding video")

# StreamingPlayer implementing relevant interfaces
class StreamingPlayer(Playable, Pausable, Stoppable):
    def play(self):
        print("Streaming content")

    def pause(self):
        print("Pausing stream")

    def stop(self):
        print("Stopping stream")

# Example usage
audio_player = AudioPlayer()
audio_player.play()
audio_player.pause()

video_player = VideoPlayer()
video_player.rewind()

streaming_player = StreamingPlayer()
streaming_player.play()
