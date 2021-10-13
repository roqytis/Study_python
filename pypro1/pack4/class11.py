#다중상속 : 가전제품의 소리 조절 기능(메소드)의 이름을 동일하게 주고 다형성 처리

class ElecProduct:
    volume = 0
    
    def volumeControl(self, volume):
        pass
    
class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume += volume
        print('티비의 소리 크기: ',self.volume)
        
class ElectRadio(ElecProduct):
    def volumeControl(self, volume):
        vol =volume
        self.volume +=vol
        print('라디오의 소리 크기: ', self.volume)
        
    def showProduct(self):
        print('라디오 고유 메소드')
        
tv= ElecTv()
tv.volumeControl(5)
tv.volumeControl(-2)

print()
radio = ElectRadio()
radio.volumeControl(7)
radio.volumeControl(2)
radio.showProduct()

print('다형성 --------------')
kbs =tv
kbs.volumeControl(3)
print()
kbs =radio
kbs.volumeControl(3)