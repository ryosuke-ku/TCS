	public static boolean deleteDir(File dir) {
		if (null == dir || !dir.exists())
			return false;
		if (!dir.isDirectory())
			throw new RuntimeException("\"" + dir.getAbsolutePath()
					+ "\" should be a directory!");
		File[] files = dir.listFiles();
		boolean re = false;
		if (null != files) {
			if (files.length == 0)
				return dir.delete();
			for (File f : files) {
				if (f.isDirectory())
					re |= deleteDir(f);
				else
					re |= f.delete();
			}
			re |= dir.delete();
		}
		return re;
	}
