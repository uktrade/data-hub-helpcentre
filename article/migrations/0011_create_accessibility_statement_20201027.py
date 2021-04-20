import datetime
import json

from django.db import migrations
from django.contrib.auth import get_user_model

from wagtail.core.models import Page


def create_accessibility_page(apps, schema_editor):
    ContentType = apps.get_model("contenttypes.ContentType")
    HomePage = apps.get_model("home.HomePage")
    ArticlePage = apps.get_model("article.ArticlePage")
    Locale = apps.get_model("wagtailcore.Locale")
    home_page = Page.objects.filter(slug="home").first()

    article_content_type, _ = ContentType.objects.get_or_create(
        model="articlepage", app_label="article",
    )

    parent = Page.objects.filter(slug=home_page.slug).first()

    current_time = datetime.datetime.now()

    blocks = []

    blocks.append(
        {
            "type": "paragraph",
            "value": """
    <p class="govuk-body">This website, Data Services Help Centre, is run by the Department for International Trade (DIT).
        It allows users to find information and help regarding the folowing services:
    </p>

    <h4 class="govuk-heading-s">Data Hub</h4>
    <p>Data Hub is DIT's customer relationship management system.</p>

    <h4 class="govuk-heading-s">Data Workspace</h4>
    <p>Data Workspace is DIT's central reporting and analysis platform.</p>

    <h4 class="govuk-heading-s">Market Access</h4>
    <p>Market Access is DIT's trade barriers reporting and management service.</p>

    <h2 class="govuk-heading-m">This accessibility statement</h2>

    <p class="govuk-body">This accessibility statement applies to the Data Services Help Centre website.</p>
    <p class="govuk-body">We want as many people as possible to be able to use this website.
    For example, that means you should be able to:</p>

    <ul class="govuk-list govuk-list--bullet">
        <li class="govuk-body">change colours, contrast levels and fonts</li>
        <li class="govuk-body">zoom in up to 300% without the text spilling off the screen</li>
        <li class="govuk-body">navigate most of the website using just a keyboard</li>
        <li class="govuk-body">navigate most of the website using speech recognition software</li>
        <li class="govuk-body">listen to most of the website using a screen reader (including the most
            recent versions of JAWS, NVDA and VoiceOver)
        </li>
    </ul>

    <p class="govuk-body">We've also tried to make the website text simple to understand.</p>
    <p class="govuk-body"><a class="govuk-link" href="https://mcmw.abilitynet.org.uk/">AbilityNet</a>
        has advice on making your device easier to use if you have a disability.
    </p>

    <h3 class="govuk-heading-s">How accessible this website is</h3>

    <p class="govuk-body">We know some parts of this website are not fully accessible:</p>

    <ul class="govuk-list govuk-list--bullet">
        <li class="govuk-body">Some navigation mechanisms do not work with screen readers.</li>
    </ul>

    <h3 class="govuk-heading-s">Feedback and contact information</h3>

    <p class="govuk-body">If you need information on this website in a different format like accessible PDF,
        large print, easy read, audio recording or braille, please contact:
    </p>
    <ul class="govuk-list govuk-list--bullet">
        <li class="govuk-body">email <a class="govuk-link" href="mailto:liveservices@digital.trade.gov.uk">liveservices@digital.trade.gov.uk</a></li>
    </ul>

    <p class="govuk-body">We'll consider your request and get back to you in 2 days.</p>

    <h2 class="govuk-heading-m">Reporting accessibility problems with this website</h2>

    <p class="govuk-body">The Live Services Team is always looking to improve the accessibility of this website.
        If you find any problems that are not listed on this page or think this website is not meeting accessibility
        requirements, please email the Live Services team at:
        <a class="govuk-link" href="mailto:liveservices@digital.trade.gov.uk">liveservices@digital.trade.gov.uk</a>
    </p>

    <p class="govuk-body">The Live Services team will review your request and get back to you in 2 working days.</p>

    <h2 class="govuk-heading-m">Enforcement procedure</h2>

    <p class="govuk-body">If you contact us with a complaint and you're not happy with our response contact the
        <a class="govuk-link" href="https://www.equalityadvisoryservice.com/">
            Equality Advisory and Support Service (EASS)
        </a>
    </p>

    <p class="govuk-body">The Equality and Human Rights Commission (EHRC) is responsible for enforcing the
        Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018
    (the 'accessibility regulations').</p>

    <h2 class="govuk-heading-m">Technical information about this website's accessibility</h2>

    <p class="govuk-body">The Government Digital Service is committed to making its websites accessible,
        in accordance with the Public Sector Bodies (Websites and Mobile Applications) (No. 2)
        Accessibility Regulations 2018.
    </p>

    <h2 class="govuk-heading-m">Non-accessible content</h2>

    <p class="govuk-body">The content that is not accessible is outlined below with details of:</p>

    <ul class="govuk-list govuk-list--bullet">
        <li>where it fails the success criteria</li>
        <li>planned dates for when issues will be fixed</li>
    </ul>

    <h3 class="govuk-heading-s">Content that fails the success criteria</h3>

    <ul class="govuk-list govuk-list--bullet">
        <li class="govuk-body">Aria attributes need to be amended to match their roles</li>
        <li class="govuk-body">Buttons need accessible names</li>
        <li class="govuk-body">Form elements need associated labels</li>
        <li class="govuk-body">Heading elements should be descending order</li>
    </ul>

    <p class="govuk-body">We plan to fix these issues by the end of January 2021.</p>

    <h2 class="govuk-heading-m">Disproportionate burden</h2>

    <p class="govuk-body">Not applicable</p>

    <h2 class="govuk-heading-m"><a class="govuk-link" href="
        https://www.gov.uk/">GOV.UK</a> services</h2>

    <p class="govuk-body">Each service has its own accessibility page, with details of how accessible the
        service is, how to report problems and how to request information in an alternative format.
        You can access these pages from the footer inside the service.
    </p>

    <h2 class="govuk-heading-m">What we're doing to improve accessibility</h2>

    <p class="govuk-body">This website will be tested specifcally for accessibility during January 2021.</p>

    <p class="govuk-body">Live Services will test a sample of pages to cover the different types of content used in the
        Financial Forecast Tool. These are:
    </p>

    <ul class="govuk-list govuk-list--bullet">
        <li class="govuk-body">The homepage</li>
        <li class="govuk-body">A sample of article home pages</li>
        <li class="govuk-body">A sample of article pages</li>
    </ul>

    <p class="govuk-body">Live Services will test the navigation bar that appears at the top of every
        page on the website.
    </p>

    <p class="govuk-body">Live Services also plan to do the following manual tests by the end of October 2020.</p>

    <ul class="govuk-list govuk-list--bullet">
        <li>Check that where tabs are used the order is logical</li>
        <li>Check that interactive elements can be focussed using the keyboard</li>
        <li>Check that interactive elements show their state and what they should be used for</li>
        <li>Check that page focus is not trapped</li>
        <li>Check that any custom interactive elements have labels</li>
        <li>Check that custom interactive elements use ARIA roles</li>
        <li>Check the visual order of content on the page follows the samew order as the DOM</li>
        <li>Check that any offscreen items cannot be seen by assistive technologies</li>
        <li>Check for the appropriate use of HTML5 landmark elements</li>
    </ul>

    <p class="govuk-body">The Live Services team works hard to ensure that this tool
        and the codebase it uses is accessible.
    </p>

    <p class="govuk-body">Where possible, the team aims to research components and patterns with a
        representative range of users, including those with disabilities.
    </p>

    <h2 class="govuk-heading-m">How we test this website</h2>
    <p class="govuk-body">This website was and is currently being tested for compliance with the Web Content Accessibility
    Guidelines V2.1 level A and level AA, and these tests have been carried out internally.</p>


    <h2 class="govuk-heading-m">Statement history</h2>

    <p class="govuk-body">This statement was prepared on 28.10.2020.</p>
        """,
        },
    )

    body = json.dumps(blocks)
    locale = Locale.objects.filter(language_code="en").first()

    accessibility_page_instance = ArticlePage(
        content_type=article_content_type,
        date=current_time,
        intro="Accessibility Statement for Data Services Help Centre",
        body=body,
        title="Accessibility Statement",
        slug="accessibility-statement",
        locale=locale,
    )

    parent.add_child(instance=accessibility_page_instance)
    parent.save()


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0010_auto_20200206_1524"),
        ("home", "0005_homepage_show_recent_child_articles"),
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
    ]

    operations = [
        migrations.RunPython(create_accessibility_page),
    ]
