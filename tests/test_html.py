import pytest

@pytest.mark.parametrize(
    'url_suffix, slug', [
        ('/travel/', 'travel'),
    ]
)
@pytest.mark.django_db
def test_category_page_contents(client, url_suffix, slug):
    url = f'/category{url_suffix}'
    response = client.get(url)
    msg_slug = '<slug>'
    msg_url = url.replace(slug, msg_slug)
    slug_found_in_page_html = slug in response.content.decode()
    assert slug_found_in_page_html, (
        f'Убедитесь, что на странице `{msg_url}` '
        f'отображается текст `{slug}`.'
    )
