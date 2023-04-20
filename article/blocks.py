from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock


class EmbedVideoBlock(blocks.StructBlock):
    """Only used for Video Card modals."""

    video = EmbedBlock(
        help_text="Paste a URL from Microsoft Stream or Youtube. Please "
        "use the page URL rather than the URL from the embed code."
    )

    class Meta:
        template = "blocks/video_embed.html"
        icon = "media"
        label = "Embed Video"
