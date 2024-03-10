import re

REGEX_CALLOUT_BLOCKS = {
    "obsidian": r"^([ \t]*)((?:> ?)+) *\[!([^\]]*)\]([\-\+]?)(.*)?\n?([ \t]*>.*\n?)*$"
    # (1) Leading white spaces (tabs and spaces)
    # (2) All leadning '>' symbol
    # (3) Callout type
    # (4) Folable symbol
    # (5) Callout title
    # (6) The contents of callout
}

REGEX_CALLOUT_HEADER = {
    "obsidian": r""
}

class Callout():
    """
    The class of callout which can be easily transformed into other styles
    """

    def __init__(self,style:str="common",foldable:str="",type:str=None,title:str="",content:str="") -> None:
        """Create a callout class that has 5 parts

        - `style` : Denote the style of the callout. `'obsidian'` and `'common'` is available. Default `'common'`
        - `type` : Type of the callout, which can be select among ['note','warning']
        - `foldable` : Foldable symbol. Like '+', '-' in Obsidian. Default ''
        - `title` : The title of callout.
        - `content` : The content of callout.
        """

        self.style = style
        self.type = type
        self.foldable = foldable
        self.title = title
        self.content = content

    def to_str(self,target:str=""):
        # exec(f"return to_{target}(self,)")
        pass


# Function for to_str in Callout classes

def to_obsidian(source:Callout) -> str:
    content = f">[!{source.type}]{source.foldable} {source.title}\n"
    
    for s in source.content.split('\n'):
        