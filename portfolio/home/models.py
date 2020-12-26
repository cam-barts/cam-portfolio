from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from django_prometheus.models import ExportModelOperationsMixin

from wagtail_blocks.blocks import (
    # HeaderBlock,
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
from portfolio.blocks import ParallaxBlock, MyCodeBlock, TimelineBlock, MyHeaderBlock
from wagtailmetadata.models import MetadataPageMixin


class FlexPage(ExportModelOperationsMixin("flex_page"), MetadataPageMixin, Page):
    body = StreamField(
        [
            ("header", MyHeaderBlock()),
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
            ("Timeline", TimelineBlock()),
        ],
        blank=True,
    )
    author_twitter_handle = models.CharField(max_length=15)
    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
        FieldPanel("author_twitter_handle"),
    ]


class ResumePage(
    ExportModelOperationsMixin("resume_page"), MetadataPageMixin, BaseResumePage
):
    pass


class IndexPage(ExportModelOperationsMixin("index_page"), MetadataPageMixin, Page):
    body = StreamField(
        [
            ("header", MyHeaderBlock()),
            ("Parallax", ParallaxBlock()),
        ],
        blank=True,
    )

    author_twitter_handle = models.CharField(max_length=15)
    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
        FieldPanel("author_twitter_handle"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = Page.objects.child_of(self).live().public().specific()
        return context
