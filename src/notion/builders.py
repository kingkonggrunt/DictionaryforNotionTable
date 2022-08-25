class RichTextBuilder:
    def __init__(self):
        self.content = []
        self.patch = {'rich_text': None}
        
    def add_rich_text(self, text: str, italic: bool=None, bold: bool=None, color=None):
        annotations = {}
        if italic:
            annotations['italic'] = italic
        if bold:
            annotations['bold'] = bold
        if color:
            annotations['color'] = color
            
        self.content.append({
            "type": "text",
            "text": {
                'content': text
            },
            "annotations": annotations
        })
        
    def new_line(self):
        annotations = {}
        self.content.append({
            "type": "text",
            "text": {
                'content': '\n'
            },
            "annotations": annotations
    })
        
    def get_patch(self) -> dict:
        patch = self.patch
        patch['rich_text'] = self.content
        return patch