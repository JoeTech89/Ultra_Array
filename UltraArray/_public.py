def check_key(key: str, against: list):
	count = 0
	for k in against:
		if k == key or k == key+str(count):
			count += 1
	if count > 0:
		key = key+str(count)
	return key
# ================================================
