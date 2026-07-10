import pytest

@pytest.mark.parametrize(
    "url, slug",
    [
        ("/category/category_slug/", "category_slug"),
        ("/category/another_slug/", "another_slug"),
    ],
)
def test_category_page_contents(try_get_url, url, slug):  # ✅ передаём фикстуру аргументом
    response = try_get_url(url)  # ✅ вызываем уже подготовленную фикстуру
    msg_slug = "<slug>"
    msg_url = url.replace(slug, msg_slug)
    slug_found_in_page_html = slug in response.content.decode()
    assert slug_found_in_page_html, (
        f"Убедитесь, что на странице `{msg_url}` "
        f"отображается текст `{msg_slug}`."
    )
