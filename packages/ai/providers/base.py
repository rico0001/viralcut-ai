class AIProvider:
    def __init__(self):
        pass

    def validate_input(self, input_data):
        raise NotImplementedError("Subclasses should implement this method.")

    def process(self, input_data):
        raise NotImplementedError("Subclasses should implement this method.")

    def generate_metadata(self, processed_data):
        raise NotImplementedError("Subclasses should implement this method.")