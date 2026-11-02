"""Reuse the genericliteral appender; earlier59examples remain unchanged."""
text=(BASE/'h9_baer_nonflat_F3_extensions/deliver.py').read_text()
text=text.replace('h9_baer_nonflat_F3_extensions','h9_baer_changed_base_refresh')
text=text.replace('nonflat Baer13','Baer changed-base refresh').replace('NonflatF3-planeBaer13cap0','Baer13changedbaseplusallowedanchors')
text=text.replace('非flat F3-plane Baer13复用rank-nullity核心覆盖','Baer13邻域复用rank-nullity核心覆盖')
exec(compile(text,str(OUT/'literal_appender.py'),'exec'))
