from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class ParallaxBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=False, help_text="Text to overlay parallax")
    img = ImageChooserBlock(required=True, help_text="Image for parallax")

    class Meta:
        icon = "fa-caret-square-o-down"
        label = "Parallax"
        template = "parallax.html"


class MyCodeBlock(CodeBlock):
    class Meta:
        icon = "code"
        template = "code_block.html"
        form_classname = "code-block struct-block"
        form_template = "wagtailcodeblock/code_block_form.html"
