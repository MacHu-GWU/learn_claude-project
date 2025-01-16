Converting Content into LLM Friendly Markdown
==============================================================================


Why Convert Documents for LLM Processing
------------------------------------------------------------------------------
In today's AI-driven world, Large Language Models (LLMs) have become powerful tools for processing and analyzing documents. While many LLMs can directly consume PDFs, Word documents, and web content, these formats often come with inherent challenges. Documents in their native format typically contain XML-based structural markup, formatting tags, and metadata that create noise during processing. This excess information can interfere with the LLM's ability to understand and work with the core content effectively. Converting these documents into a clean, structured format like Markdown offers significant advantages. Markdown not only preserves the essential content but also captures document structure through its intuitive header and bullet point syntax. This hierarchical representation helps LLMs better understand the relationships between different parts of the document, leading to improved processing and more accurate results. Whether you're dealing with enterprise documentation in Confluence, web pages, PDFs, or Word documents, having a reliable conversion process to create LLM-friendly content is crucial for maximizing the value of your AI interactions.


Tools for Converting Documents to Markdown
------------------------------------------------------------------------------
- `markdownify Python library <https://github.com/matthewwithanm/python-markdownify>`_: Very good Python library for converting HTML to Markdown, it support many HTML tags and attributes. This is actually the tool that a lot of online HTML to Markdown converters use, such as `Code Beautify HTML to Markdown Tool <https://codebeautify.org/html-to-markdown>`_, `HTML to Markdown Converter <https://htmlmarkdown.com/>`_.

.. dropdown:: test_markdownify.py

    .. literalinclude:: ./markdownify/test_markdownify.py
       :language: python
       :linenos:

- `Pandoc, Converting a web page to markdown <https://pandoc.org/demos.html>`_: not working very well, it will generate a lot of noise in markdown. A lot of HTML to Markdown converter online tools use Pandoc as the backend, such as `Cloudconvert <https://cloudconvert.com/html-to-md>`_
- `Jina Reader API <https://jina.ai/reader>`_: Convert a URL to LLM-friendly input, by simply adding r.jina.ai in front. It also offer paid API for more advanced features.
- `JsonGPT <https://jsongpt.com/converter/url-to-markdown>`_: jsongpt is a powerful tool to use structured JSON as input for LLM and get the output in JSON as well, it comes with a online tool to convert any URL to markdown.
- `Confluence Page API <https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get>`_ and `Atlassian Document Parser <https://github.com/MacHu-GWU/atlas_doc_parser-project>`_: these two work together can convert Atlassian Confluence page or JIRA issue to Markdown.
