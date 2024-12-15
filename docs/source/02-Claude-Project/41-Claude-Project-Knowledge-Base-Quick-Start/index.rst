Claude Project Knowledge Base Quick Start
==============================================================================


Overview
------------------------------------------------------------------------------
The Claude Project Knowledge Base is a powerful feature that enables users to upload and store information in various file formats. This allows Claude to retain and utilize the uploaded content across all chats in the project without requiring repetitive input.


Knowledge Base File Format Test
------------------------------------------------------------------------------
Claude Project Knowledge Base supports multiple file formats, but the file size and processing differ by format. For example, let’s consider this sample document: `Claude Project Knowledge Base Sample Document <https://docs.google.com/document/d/12njw_UxM-1Gc8xo2gReicsDoxqSio3Ap6WASUQ8TiCE/edit?tab=t.0>`_.

The document contains 2,852 words and 14,637 characters (excluding spaces). I exported it in four formats—Word, PDF, Markdown, and HTML—and uploaded them to a test Claude Project (`POC Project <https://claude.ai/project/325cef61-de73-4b2a-972b-a05b31c3ca6c>`_).

- Word: 15KB, 3%
- PDF: 79KB, 3%
- Markdown: 18KB, 3%
- HTML: 30KB, 6%

**Here’s what I found**:

- Despite differences in file size, all formats (except HTML) occupied the same Knowledge Base space: **3%**.
- HTML files occupied **6%** due to Claude interpreting HTML tags as part of the data.

This behavior suggests that Claude preprocesses files before storing them in the Knowledge Base, extracting and retaining only essential content for use in Retrieval-Augmented Generation (RAG).


Claude Contextual Retrieval in Knowledge Base
------------------------------------------------------------------------------
One of the standout features of Claude Projects is the **Knowledge Base**, which allows users to upload relevant documents and avoid re-entering information in every chat. This capability relies on advanced RAG (Retrieval-Augmented Generation) technology, but with enhancements unique to Claude’s **Contextual Retriever**.

According to this blog post `Claude Contextual Retrieval vs RAG: How is it different? <https://blog.getbind.co/2024/09/25/claude-contextual-retrieval-vs-rag-how-is-it-different/>`_, Claude’s implementation of RAG is augmented with its Contextual Retriever. Instead of simply appending retrieved content as context tokens in the chat, the retriever:

1. **Searches the Knowledge Base** for relevant content.
2. **Enhances the retrieved information** by adding contextual details.
3. Combines this enriched context with the user’s prompt to generate the final response.

This unique approach ensures more accurate, insightful, and context-aware responses compared to traditional RAG implementations. For example, when you mention "section1234" in a chat, Claude can locate the corresponding section in the Knowledge Base and provide precise, relevant information. This enhanced retrieval greatly improves the user experience and efficiency of interactions.


Reference
------------------------------------------------------------------------------
- `Claude News - Collaborate with Claude on Projects <https://www.anthropic.com/news/projects>`_
