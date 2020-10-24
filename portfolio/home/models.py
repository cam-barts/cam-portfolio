from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail_blocks.blocks import (
    HeaderBlock,
    ListBlock,
    ImageTextOverlayBlock,
    CroppedImagesWithTextBlock,
    ListWithImagesBlock,
    ThumbnailGalleryBlock,
    ChartBlock,
    MapBlock,
    ImageSliderBlock,
)
from wagtailstreamforms.blocks import WagtailFormBlock
from wagtail_resume.models import BaseResumePage
from portfolio.blocks import ParallaxBlock, MyCodeBlock
from wagtailmetadata.models import MetadataPageMixin


class HomePage(MetadataPageMixin, Page):
    body = StreamField(
        [
            ("header", HeaderBlock()),
            ("list", ListBlock()),
            ("image_text_overlay", ImageTextOverlayBlock()),
            ("cropped_images_with_text", CroppedImagesWithTextBlock()),
            ("list_with_images", ListWithImagesBlock()),
            ("thumbnail_gallery", ThumbnailGalleryBlock()),
            ("chart", ChartBlock()),
            ("map", MapBlock()),
            ("image_slider", ImageSliderBlock()),
            ("form", WagtailFormBlock()),
            ("Parallax", ParallaxBlock()),
            ("Code", MyCodeBlock()),
        ],
        blank=True,
    )
    author_twitter_handle = models.CharField(max_length=15)
    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
        FieldPanel("author_twitter_handle"),
    ]


class ResumePage(MetadataPageMixin, BaseResumePage):
    pass
