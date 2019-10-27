    protected String documentToString(Document document, boolean omitProlog) throws Exception {
        TransformerFactory transFactory = TransformerFactory.newInstance();

        // Indentation not supported on Android 2.2
        //transFactory.setAttribute("indent-number", 4);

        Transformer transformer = transFactory.newTransformer();

        if (omitProlog) {
            // TODO: UPNP VIOLATION: Terratec Noxon Webradio fails when DIDL content has a prolog
            // No XML prolog! This is allowed because it is UTF-8 encoded and required
            // because broken devices will stumble on SOAP messages that contain (even
            // encoded) XML prologs within a message body.
            transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
        }

        // Again, Android 2.2 fails hard if you try this.
        //transformer.setOutputProperty(OutputKeys.INDENT, "yes");

        StringWriter out = new StringWriter();
        transformer.transform(new DOMSource(document), new StreamResult(out));
        return out.toString();
    }
