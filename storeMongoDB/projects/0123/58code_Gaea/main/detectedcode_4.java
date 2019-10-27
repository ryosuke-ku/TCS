    public static ServiceConfig GetConfig(String serviceName) throws Exception {
        File f = new File(GaeaConst.CONFIG_PATH);
        if (!f.exists()) {
            throw new Exception("gaea.config not fond:" + GaeaConst.CONFIG_PATH);
        }

        Element xmlDoc = XMLHelper.GetXmlDoc(GaeaConst.CONFIG_PATH);
        XPathFactory xpathFactory = XPathFactory.newInstance();
        XPath xpath = xpathFactory.newXPath();
        Node serviceNode = (Node) xpath.evaluate("//Service[@name='" + serviceName + "']", xmlDoc, XPathConstants.NODE);
        if(serviceNode == null){
        	printExceprion(0,serviceName);
        }
        
        ServiceConfig config = new ServiceConfig();
        config.servicename = serviceNode.getAttributes().getNamedItem("name").getNodeValue();
        Node idNode = serviceNode.getAttributes().getNamedItem("id");
        if(idNode == null){
        	printExceprion(4,serviceName);
        }
        config.serviceid = Integer.parseInt(idNode.getNodeValue());
        Node xnSocketPool = (Node) xpath.evaluate("Commmunication/SocketPool", serviceNode, XPathConstants.NODE);
        if(xnSocketPool == null){
        	printExceprion(1,serviceName);
        }
        config.SocketPool = new SocketPoolProfile(xnSocketPool);

        Node xnProtocol = (Node) xpath.evaluate("Commmunication/Protocol", serviceNode, XPathConstants.NODE);
        if(xnProtocol == null){
        	printExceprion(2,serviceName);
        }
        config.protocol = new ProtocolProfile(xnProtocol);
        
        /**
