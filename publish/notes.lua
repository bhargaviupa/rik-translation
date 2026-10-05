-- Turn pandoc footnotes into inline spans so CSS (float: footnote) can place them at page foot.
function Note(el)
  local inl = pandoc.utils.blocks_to_inlines(el.content, {pandoc.Space()})
  return pandoc.Span(inl, {class = "fn"})
end
