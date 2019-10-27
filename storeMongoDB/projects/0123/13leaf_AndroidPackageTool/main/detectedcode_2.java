	public static String getParentDir(String path1, String path2)
			throws IOException {
		if (path1.contains(".") || path2.contains(".")) {// not a canonicalPath
			path1 = new File(path1).getCanonicalPath();
			path2 = new File(path2).getCanonicalPath();
		}
		char[] originalChars = path1.toCharArray();
		char[] targetChars = path2.toCharArray();
		int i = -1;
		while (++i < originalChars.length && i < targetChars.length) {// to get the latest both public start
			if (originalChars[i] != targetChars[i]) {
				--i;// back
				break;
			}
		}
		if(i==-1) return null;
		else return path2.substring(0, i);
	}
