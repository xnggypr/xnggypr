import gifos

t = gifos.Terminal(width=800, height=600, xpad=5, ypad=5, font_size=15)
t.gen_text(text="Hello World!", row_num=1)
t.gen_text(text="Hello, VizXtreme and ukriu!", row_num=2)
github_stats = gifos.utils.fetch_github_stats(
    user_name="xnggypr"
)  # needs GITHUB_TOKEN in .env or as environment variable
t.delete_row(row_num=1)
t.gen_text(text=f"GitHub Name: {github_stats.account_name}", row_num=1, contin=True)
t.gen_gif()
image = gifos.utils.upload_imgbb(
    file_name="output.gif", expiration=60
)  # needs IMGBB_API_KEY in .env or as environment variable
print(image.url)