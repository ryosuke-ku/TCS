	public void setCenterMember(Canvas member) {
		if (member == null) {
			center.setWidth(0);
			center.setHeight(0);
			center.setMembers();
		} else {
			member.setHeight("100%");
			member.setWidth("100%");
			center.setWidth("100%");
			center.setMembers(member);
		}
	}

