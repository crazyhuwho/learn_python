class person(object):
	"""docstring for 人类"""

	def __init__(self, name):
		super(person, self).__init__()
		self.name = name #用于记录人的名字
		self.gun = None #用于保存枪对象的引用
		self.hp = 100 #用于保存玩家的血量

	def install_bullet(self,dan_jia_temp,zi_dan_temp):
		'''把子弹撞到弹夹中'''
		#弹夹.保存子弹(子弹)
		dan_jia_temp.sava_bulllet(zi_dan_temp)

	def install_cartridge(self,gun_temp,dan_jia_temp):
		'''把弹夹安装到枪中'''
		#枪.保存弹夹(弹夹)
		gun_temp.save_cartridge(dan_jia_temp)

	def with_a_gun(self,gun_temp):
		'''老王拿起一把枪'''
		self.gun = gun_temp

	def __str__(self):
		if self.gun:
			return "%s的血量为：%d,他有枪%s"%(self.name,self.hp,self.gun)
		else:
			if self.hp>0:
					return "%s的血量为：%d,他没有枪"%(self.name,self.hp)
			else:
				return "%s已挂..."%self.name
	def pull_trigger(self,enemy):
		'''让枪打敌人'''
		#枪.开火(敌人)
		self.gun.fire(enemy)

	def decrease_hp(self,killability):
		'''根据杀伤力，掉相应的血量'''
		self.hp -= killability

class gun(object):
	"""docstring for 枪类"""

	def __init__(self, name):
		super(gun, self).__init__()
		self.name = name #用于记录枪的类型
		self.cartridge_list = None #用于记录弹夹对象的引用

	def save_cartridge(self,dan_jia_temp):
		'''用一个属性保存弹夹对象的引用'''
		self.cartridge_list = dan_jia_temp

	def __str__(self):
		return "枪的信息：%s"%(self.name)

	def fire(self,enemy):
		'''枪从弹夹中取出一发子弹，然后让这发子弹去射击敌人'''

		#先从弹夹中取出子弹
		zi_dan_temp = self.cartridge_list.pop_bullet()

		#让这个子弹去射击敌人
		if zi_dan_temp:
			#子弹.打中敌人
			zi_dan_temp.hit(enemy)
		else:
			print("弹夹中没有子弹")

class cartridge(object):
	"""docstring for 弹夹类"""

	def __init__(self, max_num):
		super(cartridge, self).__init__()
		self.max_num = max_num #用来记录弹夹的最大容量
		self.bullet_list = [] #用来记录所有子弹的引用

	def sava_bulllet(self,zi_dan_temp):
		'''将子弹对象保存'''
		self.bullet_list.append(zi_dan_temp)

	def __str__(self):
		return "弹夹的信息为%d/%d"%(len(self.bullet_list),self.max_num)

	def pop_bullet(self):
		'''弹出上面的那颗子弹'''
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None
		
class bullet(object):
			"""docstring for 子弹类"""

			def __init__(self, killability):
				super(bullet, self).__init__()
				self.killability = killability #用于记录子弹的杀伤力
			def hit(self,enemy):
				'''让敌人掉血'''

				#敌人.掉血(一颗子弹的威力)
				enemy.decrease_hp(self.killability)

		
def main():
	'''用来控制整个函数的流程'''
	#1.创建老王对象
	Mr_Wang = person("老王")

	#2.创建枪对象
	ak47 = gun("ak47")

	#3.创建弹夹对象
	dan_jia = cartridge(20)

	#4.创建一些子弹对象
	for i in range(15):
		zi_dan = bullet(10)		

		#5.老王把子弹安装到弹夹
		#老王.安装子弹到弹夹中（弹夹，子弹）
		Mr_Wang.install_bullet(dan_jia,zi_dan)

	#6.老王把弹夹安装到枪
	#老王.安装弹夹到枪中(枪,弹夹)
	Mr_Wang.install_cartridge(ak47,dan_jia)

	#test:测试弹夹的信息
	print(dan_jia)

	#test:测试枪的信息
	print(ak47)

	#7.老王拿枪
	#老王.拿枪(枪)
	Mr_Wang.with_a_gun(ak47)
	
	#test:测试老王对象
	print(Mr_Wang)

	#8.创建敌人对象
	trump = person("特兰普蠢蛋")
	print(trump)

	#9.老王用枪射击敌人
	#老王.扣扳机(敌人)
	for i in range(0,10):
		Mr_Wang.pull_trigger(trump)
		print(dan_jia)
		print(trump)

if __name__ == '__main__':
	main()



[结果输出]
[root@os-python python]# python shooting.py 
弹夹的信息为15/20
枪的信息：ak47
老王的血量为：100,他有枪枪的信息：ak47
特兰普蠢蛋的血量为：100,他没有枪
弹夹的信息为14/20
特兰普蠢蛋的血量为：90,他没有枪
弹夹的信息为13/20
特兰普蠢蛋的血量为：80,他没有枪
弹夹的信息为12/20
特兰普蠢蛋的血量为：70,他没有枪
弹夹的信息为11/20
特兰普蠢蛋的血量为：60,他没有枪
弹夹的信息为10/20
特兰普蠢蛋的血量为：50,他没有枪
弹夹的信息为9/20
特兰普蠢蛋的血量为：40,他没有枪
弹夹的信息为8/20
特兰普蠢蛋的血量为：30,他没有枪
弹夹的信息为7/20
特兰普蠢蛋的血量为：20,他没有枪
弹夹的信息为6/20
特兰普蠢蛋的血量为：10,他没有枪
弹夹的信息为5/20
特兰普蠢蛋已挂...
