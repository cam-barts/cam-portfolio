from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from wagtail_blocks.blocks import HeaderBlock


class ParallaxBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=False, help_text="Text to overlay parallax")
    img = ImageChooserBlock(required=True, help_text="Image for parallax")
    speed = blocks.FloatBlock(
        required=True,
        max_value=1.0,
        min_value=0.0,
        default=0.2,
        help_text="Speed to run the parallax",
    )

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


class TimelineSectionBlock(blocks.StructBlock):
    blurbs = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("blurb_header", blocks.CharBlock(required=True)),
                ("blurb_content", blocks.RichTextBlock(required=True)),
            ]
        )
    )


class TimelineBlock(blocks.StructBlock):
    sections = blocks.ListBlock(TimelineSectionBlock())

    class Meta:
        icon = "arrows-up-down"
        label = "Timeline"
        template = "timeline.html"


class MyHeaderBlock(HeaderBlock):
    text = blocks.RichTextBlock(required=True, features=["accent"])
