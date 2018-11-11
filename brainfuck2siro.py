import sys

commands = str.maketrans({
	'>' : 'いーねっ！',
	'<' : 'ｷｭｰｲ',
	'+' : 'おほほい',
	'-' : 'ぱいーん',
	'.' : 'なんて日だ！',
	',' : 'ズンドコズンドコ♪',
	'[' : '白組さん',
	']' : '救済'
})

def main():
	try:
		fname = sys.argv[1]
		input = open(fname, 'r').read()
		output = input.translate(commands)
		print(output)
		
	except Exception as e:
		print(e)
		sys.exit('USAGE: python brainfuck2siro.py <filename>')

if __name__ == '__main__':
	main()
