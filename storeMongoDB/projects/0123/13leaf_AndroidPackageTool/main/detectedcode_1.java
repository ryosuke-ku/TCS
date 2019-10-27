	public static String toRelativePath(File original, File target)
			throws IOException {
		String relativePath = "";
		String originalPath = original.getCanonicalPath();
		String targetPath = target.getCanonicalPath();
		String publicDir = getParentDir(originalPath, targetPath);
		
		if(null==publicDir) throw new IOException(String.format("original:%s\ntarget:%s have no public directory!", originalPath,targetPath));
		if(originalPath.equals(publicDir)) return "."+targetPath.substring(publicDir.length(), targetPath.length());
		relativePath=toParentRelative(originalPath,publicDir);
		return "."+relativePath+targetPath.substring(publicDir.length(),targetPath.length());
	}
