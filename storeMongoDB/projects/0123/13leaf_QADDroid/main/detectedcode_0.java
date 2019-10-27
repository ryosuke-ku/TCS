	public static void write(File f, Object obj) {
		if (null == f || null == obj)
			return;
		if (f.isDirectory())
			throw Lang.makeThrow("Directory '%s' can not be write as File", f);

		try {
fragmentStart=originUrl.indexOf('#');//search param end
		String baseUrl=originUrl;
		String fragment="";
		if(paramStart!=-1){
			baseUrl=originUrl.substring(0,paramStart);
		}
		if(paramStart==-1 && fragmentStart!=-1){
			baseUrl=originUrl.substring(0,fragmentStart);
		}
		if(fragmentStart!=-1){
			fragment=originUrl.substring(fragmentStart+1);
		}
		String baseParam="";
		if(paramStart!=-1 && fragmentStart!=-1){
			baseParam=originUrl.substring(paramStart+1,fragmentStart);
		}else if(paramStart!=-1){
			baseParam=originUrl.substring(paramStart+1);
		}
		if(baseParam.length()!=0){
			param=baseParam+"&"+param;
		}
		
		String outUrl= baseUrl+"?"+param+(fragment.length()==0?"":"#"+fragment);
		return outUrl;
	}
