	public Character convertToCharacter(Object obj) {
		String str = obj.toString();
		if(str.length() > 1) {
			str = str.replaceFirst("\"", "");
		}
		if(!str.equals(null) && !str.equals("")){
			return new Character(str.charAt(0));
		}
		return new Character('\0');
	}

