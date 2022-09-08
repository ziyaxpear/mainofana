
# PIL : açık kaynak kodlu grafik işleme kütüphanesidir. Bu kütüphane,
# içinde barındırdığı hazır fonksiyonlar sayesinde programcıya üstün bir grafik işleme imkânı sunar.
# Birçok grafik türünü açıp kaydetme yeteneği ile birlikte çizim, düzenleme,
# filtreleme gibi işlemlerde kullanılabilecek fonksiyonlara sahiptir.
# lsb en önemsiz bit   \\least important bit
##############################################3
# io : Senkron ve asenkron olmak üzere iki tür I/O işlemi bulunmaktadır.
# Senkron I/O işlemlerinde uygulama bloklanmakta yani I/O işlemi tamamlanana kadar beklenilmektedir.
# Asenkron I/O işlemlerinde ise olayın tamamlanması beklenmez,
# uygulama bloklanmaksızın bu süreç boyunca başka işlemler yapılabilir
# buradaki işlevi vewrilen dosyaları türleri ile açmak örnek f= open("myfile.jpg","r",encoding,"utf-8") gibi bir
# planmlama çalıştırma için bu kütüphane kulannıldı


# Bazı Faydalı fonksiyonlar ============================
# iki görüntü arasındaki 'Ortalama Kare Hatası', iki görüntü arasındaki kare farkının toplamıdır;
# NOT: iki resim aynı boyuta sahip olmalıdır
# asytpe: veri analizinde kullanılan bir işlemdir asynic kütüphanesinden çekilir.
# shape :bir numphy fonksiyonudur ve eleman ekleme işi yapar
#
# streamlit_app.py


try:
    import streamlit.components.v1 as components
    import js2py
    from io import BytesIO
    from PIL import Image
    import streamlit as st
    import numpy as np
    import base64
    import warnings

    warnings.filterwarnings("ignore")


except Exception as e:
    print(e)
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

astyle = """
display: inline;
width: 200px;
height: 40px;
background: #F63366;
padding: 9px;
margin: 8px;
text-align: center;
vertical-align: center;
border-radius: 5px;
color: white;
line-height: 25px;
text-decoration: none;
"""

st.set_page_config(
    page_title="Steganografik Bir Yapı Düzeni Uygulaması",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",

)

tabs = ["GİRİŞ", "Steganografi nedir", "Hakkında", "Vizyon", "Misyon ve Resim Gizleme","Örnek Proje Görselleri"]
page = st.sidebar.radio("Sekmeler", tabs)
image1 = Image.open("mona3.png")
image2 = Image.open("heredot.png")
image3 = Image.open("tablet.png")
image4 = Image.open("kalem.png")
image5 = Image.open("blokzinciri nedir devam.png")
image8 = Image.open("meta.png")
video_file = open('Steganografii.mp4', 'rb')
video_bytes = video_file.read()
image6 = Image.open("neden blok zinciri.png")
image7 = Image.open("blokzincirinedir.png")

if page == "GİRİŞ":
    st.image(image8, caption="Metamask hesabı ile giriş yapın")
    st.markdown(
        "Metamask hesabı ile doğrulama yapmazsanız Her hangi bir veri kaydı gerçekleştiremezsiniz. Lütfen aşağıda bulunan metamask düğmesine tıklayarak giriş yapınız")
    eval_res, fileJS = js2py.run_file("merhaba.js")
    if st.button('Metamask İle Griş Yapınız'):
        components.html(
            """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8"/>
                <link rel="stylesheet" type="text/html" href="styles.css"/>
            </head>

            <body>
                <button id="connect-button"> Connect Metamask</button>
                <script >
                    document.getElementById('connect-button').addEventListener('click',event=> {
                        let account;
                        ethereum.request({method: 'eth_requestAccounts'}).then(accounts => {
                            account = accounts[0];
                            console.log(account);

                            ethereum.request({method: 'eth_getBalance' ,params: [account, 'latest']}).then(rsult => {
                                console.log(result);
                                let wei = parseInt(result,16);
                                let balance = wei / (10**18);
                                console.log(balance + "ETH");
                            });
                        });
                    });

                </script>
            </body>
        </html>
        """
        )


else:
st.write('Goodbye')

elif page == "Steganografi nedir":
    st.image(image1, caption="Steganografi Nedir")
    st.markdown("<h1 style='text-align:center;'> Steganografi Hakkında Kısa bir Tarih</h1>", unsafe_allow_html=True)
    st.write(
        "      Steganografi, mesajı gömme yoluyla bilgiyi saklama sanatı ve bilimidir. Bu yaklaşım, bir nesnenin içerisine bir verinin gizlenmesi olarak da tanımlanabilir. Bu yaklaşımla ses, resim, video görüntüleri üzerine veri saklanabilir. Görüntü dosyaları içerisine saklanacak veriler metin dosyası olabileceği gibi herhangi bir görüntü içerisine gizlenmiş başka bir görüntü dosyası da olabilir. Steganografinin birinci amaç, bir mesajın varlığını saklamak ve bir örtülü kanal yaratmaktır. İkinci amacı mesajın içeriğini saklamak olan kriptolojinin bir parçası olarak görmektir. Bu iki tekniği beraber kullanmakta mümkündür. Fakat steganografi ile kriptografi aynı işlevi görmez. Kriptografide gizlenen içeriğin şifrelendiği bellidir ve bu yüzden şifrelendiği apaçık belli olabilir. Steganografide saklanan veri belli olmadığından bilginin istenilen kaynaklara ulaşması daha güvenli bir hal alır.  Bunun için gizli mesaj önce encrypt (şifrelenir) edilir, sonra steganografik yöntemlerle dijital bir verinin içerisine saklanabilir")

    bir_kac_hikaye = st.selectbox(
        "Aşağıda Steganografi Hakında Bir kaç Hikaye Örneği verilmiştir. İstediğinizi okuyabilirsiniz ",
        ("Heredot'un Hikayesi", "Bal Mumu Hikayesi", "Mor Ötesi Işınlar", "Günümüzde Steganografi"))
    if bir_kac_hikaye == " ":
        st.write("Hikayeleri ookumak için Seçim Yapınız")
    elif bir_kac_hikaye == "Heredot'un Hikayesi":
        st.write(
            "Herodot’un bir hikayesine göre Pers saldırısının öncesinde saçları tıraşlanan bir kölenin kafasına yazılan uyarı mesajı, saçlarının uzaması sayesinde saklanmıştır. Bu sayede, mesaj dikkat çekmeden gerekli yere ulaşabilmiş, ulaştığında da kölenin saçları tekrar kesilerek uyarı okunabilmiştir.")
        st.image(image2, caption="İnsani Steganografi")
    elif bir_kac_hikaye == "Bal Mumu Hikayesi":
        st.write(
            "Eski Yunanistan’da, insanlar mesajları tahtaya yazıp üzerini mumla kaplarlardı. Böylece cisim kullanılmamış bir tablete benzerdi öte yandan mumun eritilmesiyle birlikte içindeki gizli mesaj okunabilirdi.")
        st.image(image3)
    elif bir_kac_hikaye == "Mor Ötesi Işınlar":
        st.write(
            "Özellikle 1960’larda mor ötesi boya ile yazı yazabilen sprey ve kalemler modaydı. Bu kalemlerin yazdığı yazılar, sadece bir mor ötesi ışıkla görülebiliyordu.")
        st.image(image4)
    else:
        st.write(
            "Günümüz Dijital Dünyasında artık bir mesajı saklamak istediğimizde ya da bir dosyamızı gizlemek istediğimizde ilkel yöntemlerden ziyade dijital yöntemler kullanılabilir. Bu projede Python programlama dili yardımı ile bir veriyi kolaylıkla saklayabiliriz.")
        st.image(image5)
elif page == "Hakkında":
    st.markdown("<h1 style='text-align:center;'> Geliştirilen Web Sayfası Hakkında Bir Kaç Bilgi</h1>",
                unsafe_allow_html=True)
    st.write(
        "Geliştirlen bu web arayüzü her hangi bir ticari amaç gütmeksizin tamamı ile ücretsiz ve eğitim amaçlı kurulmuştur.")
    st.video(video_bytes)
elif page == "Vizyon":
    st.markdown("<h1 style='text-align:center;'> Genel Vizyonumuz</h1>", unsafe_allow_html=True)
    st.write(
        "Geliştirmek istidiğimiz bu Proje sayesinde insanlar verilerini daha kolay ve daha güvenilir bir yol ile hem hızlı bir şekilde hemde maliyeti en aza indirerek saklayabileceklerdir.")
    st.image(image6)

elif page == "Misyon ve Resim Gizleme":


st.markdown("<h1 style='text-align:center;'> Genel Misyonumuz</h1>", unsafe_allow_html=True)
st.write("Sizce İnsanların bilgilerini en iyi şekilde saklamanın bir yolu varmıdır?"
         " evet Vardır değil mi ?"
         "Belki size basit gelecek ama her insan bir bilgi saklamak ister ama bu bilgiyi saklarken de sürekli bir korku içinde yaşar "
         "İşte tamda bu noktada bizim projemizin asıl misyonu ortaya çıkıyor"
         "tüm insanlığa en iyi ve en güvenli şekilde nasıl bir hizmet sunabiliriz?"
         "amacımız tüm insanlığa en iyi şekilde hizmet vermek.")

st.image(image7)


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # MSE'yi döndürün, hata ne kadar düşükse, iki görüntü o kadar "benzer" olur
    return err


# BytesIO: Değişkenlerle yaptığımız gibi, io modülünün Byte IO işlemlerini kullandığımızda
# veriler bir bellek içi arabellekte bayt olarak tutulabilir.
def get_image_download_link(filename, img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = '<a href="data:file/png;base64,' + img_str + '" indir=' + filename + ' style="' + astyle + '" target="_blank">Resmi indir</a>'

    return href


#  dump . bir değer döndürmez ama verilen değeri istenilen konuma gönderir
def get_key_download_link(filename, key):
    buffered = BytesIO()
    key.dump(buffered)
    key_str = base64.b64encode(buffered.getvalue()).decode()
    href = '<a href="data:file/pkl;base64,' + key_str + '" download=' + filename + ' style="' + astyle + '" target="_blank">Download Key</a>'
    return href


# Algo 1 =======================================

# Pikseller, 8 bitlik ikili verilere göre değiştirilir ve sonunda döndürülür.
def modPix(pix, data):
    datalist = [format(ord(i), '08b') for i in data]
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Bir seferde 3 piksel çıkarma
        pix = [value for value in imdata.next()[:3] + imdata.next()[:3] + imdata.next()[:3]]

        # Piksel değeri 1 için tek yapılmalı ve 0 için bile, pix bir pikselin bir kanalıdır
        for j in range(0, 8):
            if (datalist[i][j] == '0'):
                pix[j] &= ~(1 << 0)

            elif (datalist[i][j] == '1'):
                pix[j] |= (1 << 0)

        # Her kümenin sekizinci pikseli, daha fazla okumayı durdurup durdurmayacağını söyler.
        # 0, okumaya devam et anlamına gelir; 1 mesajın bittiği anlamına gelir.
        if (i == lendata - 1):
            pix[-1] |= (1 << 0)

        else:
            pix[-1] &= ~(1 << 0)

        # yield : iteratyrler ile beraber çalışır aynı mantıkla döngülerde tekrarrı sağlar
        pix = tuple(pix)
        yield pix[0:3]  # pixel 1
        yield pix[3:6]  # pixel 2
        yield pix[6:9]  # pixel 3


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):
        # Değiştirilmiş pikselleri yeni görüntüye yerleştirme
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


# Verileri görüntüye kodlayın
def encode(filename, image, bytes):
    global c1, c2

    data = c1.text_area("Kodlanacak veriyi giriniz", max_chars=bytes)

    if (c1.button('Encode', key="1")):
        if (len(data) == 0):
            c1.error("Veri boş")
        else:
            c2.markdown('#')
            result = "Verilen veriler, verilen kapak resminde kodlanmıştır."
            c2.success(result)
            c2.markdown('####')
            c2.markdown("#### Kodlanmış resim")
            c2.markdown('######')

newimg = image.copy()
encode_enc(newimg, data)
c2.image(newimg, channels="BGR")

filename = 'encoded_' + filename

image_np = np.array(image)
newimg_np = np.array(newimg)
MSE = mse(image_np, newimg_np)
msg = "MSE: " + str(MSE)
c2.warning(msg)
c2.markdown("#")
c2.markdown(get_image_download_link(filename, newimg), unsafe_allow_html=True)


# Görüntüdeki verilerin kodunu çözün
def decode(image):
    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.next()[:3] + imgdata.next()[:3] + imgdata.next()[:3]]

        # ikili veri dizisi
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))

        if (pixels[-1] % 2 != 0):
            return data

    # sidebar. yazılmak iistenen değer ve fonksiyonları streamlite de yan tarafa yazar ,
    # md . de kullanılan href monalisa resmine ulaşır


def main():
    global c1, c2, d1, d2

    st.markdown("SAKLI PROJE")

    st.sidebar.title("Dijital Görüntü İşleme Projesi")

    md = "![1](https://miro.medium.com/max/2560/1*dQyfOpFWmSxrmdOcQgW6OQ.jpeg)"
    st.sidebar.markdown(md, unsafe_allow_html=True)

    info = """

        """
    st.sidebar.markdown(info, unsafe_allow_html=True)
    st.sidebar.subheader("Görüntü İşleme Algoritması Olarak LSB Algoritması kullanılacak: ")
    algo = st.sidebar.radio("", ["LSB II Algorithm"])

    st.sidebar.markdown(info, unsafe_allow_html=True)

    fileTypes = ["png", "jpg"]
    fileTypes1 = ["pkl"]
    st.markdown(STYLE, unsafe_allow_html=True)

    if (algo == "LSB II Algorithm"):
        st.subheader("LSB II Algoritması")
        st.write(
            "Bir ASCII karakterini kodlamak için 3 piksel (3*3 kanal = 9 değer) kullanılır. İlk 8 değerin LSB'leri ASCII'yi ikili formatta kodlar ve 9. değerin LSB'si mesajın sonu olup olmadığını göstermek için kullanılır. Veriler ilk pikselden itibaren seri olarak depolanır.")
        choice = st.radio('Seçim', ["Encode", "Decode"])
        if (choice == "Encode"):
            c1, c2 = st.columns(2)
            file = c1.file_uploader("Kapak Resmini Yükle", type=fileTypes, key="fu1")
            show_file = c1.empty()
            if not file:
                show_file.info("Lütfen bir dosya türü yükleyin: " + ", ".join(["png", "jpg"]))
                return

            im = Image.open(BytesIO(file.read()))
            filename = file.name
            w, h = im.size
            bytes = (w * h) // 3
            c1.info("maksimum veri: " + str(bytes) + " Bytes")
            encode(filename, im, bytes)

            content = file.getvalue()
            if isinstance(file, BytesIO):
                show_file.image(file)

            file.close()

        elif (choice == "Decode"):
            file = st.file_uploader("Kodlanmış Resmi Yükle", type=fileTypes, key="fu2")
            show_file = st.empty()
            if not file:
                show_file.info("Lütfen bir dosya türü yükleyin: " + ", ".join(["png", "jpg"]))
                return

            im = Image.open(BytesIO(file.read()))

            data = decode(im)

            if (st.button('Decode', key="4")):
                st.subheader("kodu çözülmüş metin")
                st.write(data)

            content = file.getvalue()
            if isinstance(file, BytesIO):
                show_file.image(file)

            file.close()


if __name__ == "__main__":
    main()
