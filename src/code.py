from bs4 import BeautifulSoup
from requests import get

class Script:
    def query(self, url):
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        tag = soup.find_all('article')
        data = []

        for i in tag:
            try:
                title = i.find('h2').text
                link = i.find('a').get('href')
                gambar = i.find('img').get('src')
                # tipe = i.find('span', class_='block mt-1').text
                data.append({
                    "judul": title,
                    "link": link,
                    "poster": gambar,
                    # "tipe": tipe,
                })
            except:
                pass

        return data

    def index(self):
        return self.query('https://www.cnnindonesia.com/')

    def nasional(self):
        return self.query('https://www.cnnindonesia.com/nasional')
    def internasional(self):
        return self.query('https://www.cnnindonesia.com/internasional')
    def ekonomi(self):
        return self.query('https://www.cnnindonesia.com/ekonomi')
    def olahraga(self):
        return self.query('https://www.cnnindonesia.com/olahraga')

    def teknologi(self):
        return self.query('https://www.cnnindonesia.com/teknologi')

    def hiburan(self):
        return self.query('https://www.cnnindonesia.com/hiburan')

    def social(self):
        return self.query('https://www.cnnindonesia.com/gaya-hidup')

    def detail(self, url):
        data = []
        try:
            req = get(url)
            print(req)
            soup = BeautifulSoup(req.text, 'html.parser')
            print(soup)
            tag = soup.find('div', class_="detail-text text-cnn_black text-sm grow min-w-0")
            gambar = soup.find('div', class_='detail-image my-5').find('img').get('src')
            judul = soup.find('h1', class_='mb-2 text-[28px] leading-9 text-cnn_black').text
            tanggal = soup.find('div', class_='text-cnn_grey text-sm mb-4').text
            body = tag.text
            data.append({
                "message": "success",
                "judul": judul,
                "poster": gambar,
                "tanggal" : tanggal,
                "body": body,
            })
        except:
            data.append({
                "message": "network error",
            })

        return data

    def search(self,q):
        return self.query('https://www.cnnindonesia.com/search/?query=' + q)

if __name__ != '__main__':
    Code = Script()