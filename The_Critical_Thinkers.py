import streamlit as st
from PIL import Image

lord_shiva=Image.open("1.jpg")
st.set_page_config(page_title="The_Critical_Thinkers",page_icon=":tada:",layout="wide") #  :tada: = emoji code
st.write(
    """<div style="text-align: center; margin-top: 10px;">
        <h3>ॐ नमः शिवाय</h3>
    </div>""",
    unsafe_allow_html=True
)
st.image(lord_shiva.resize((1500,900)))
# div = Container/element, style= attribute
Hanuman_ji =Image.open("robot1.jpg")
Arjun_ji= Image.open("robot2.jpg")
bhagvan_shiv=Image.open("robot3.jpg")
shivji_new=Image.open("robot4.jpg")
shivji_new1=Image.open("robot5.jpg")
main_image= Image.open("IMG_20240110_204218.png")
like_share=Image.open("Like_share_subscribe.png")
# like_share_new="Like_share_subscribe.png"
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
# Header Section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        # css = """
        # <style>
        # [data-testid="stAppViewContainer"]{
        #     background-image: url('https://yt3.ggpht.com/ytc/APkrFKb_hyYEPR7L6eVCVwHInw3LsvtGYzjp6Z1hWXHtmQ=s600-c-k-c0x00ffffff-no-rj-rp-mo');
        #     background-size: 1800px 1000px;
        #     color: black;
        # }
        # </style>
        # """
        # st.markdown(css, unsafe_allow_html=True)
        st.title("The Critical Thinkers")
        #st.write("@GodisOneandSupremeTruth")
        #st.subheader("'ॐ नमः शिवाय'")
        st.header(":wave: Hi, We are an ATL Team of")
        st.subheader("DAV Public School, Thermal Colony, Panipat, Haryana")
        st.markdown(
            f'<style>{open("custom.css").read()}</style>',
            unsafe_allow_html=True
        )
        st.write("[Official Facebook Page >](https://www.facebook.com/atldavpanipat/)")
    with right_column:
        st.image(main_image.resize((1200,600)))
        # resized_image= main_image.resize((200,100))
        # resized_image.save("new_image.jpg")
        # resized_image.show()


# What I do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Team Details")
        st.write("##") # To give space between two lines
        # st.subheader("We are a team of 4 team members in IRC 2023-24 whose names are as follows:")
        # # st.write("")
        # st.subheader("1. Akhil Swami, class 7th  (Team Leader)")
        # st.subheader("2. Mayank Dahiya, class 8th")
        # st.subheader("3. Harsh Sharma, class 7th")
        # st.subheader("4. Lakshay Rathi, class 6th")

        st.write("""
        We are a team of 4 team members in IRC 2023-24 whose names are as follows:
        \n 1. Akhil Swami,   class 7th   (Team Leader)
        \n 2. Mayank Dahiya, class 8th
        \n 3. Harsh Sharma,  class 7th
        \n 4. Lakshay Rathi, class 6th
        """)
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Us")
        st.write("##")  # To give space between two lines
        st.write("""We have participated in Asia's Biggest Robotics and Coding competition named IRC (International Robotics Competition) and in the Zonal Level of this competition held at Vega school, Gurugram, Haryana our team got 3rd position and qualified for the Nationals which will be held at Yamuna Sports Complex, Surajmal Vihar, New Delhi.
        """)
    with right_column:
    # st.write("""
    # chjhcjhd""")
        st.empty()
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Significance of our Team name")
        st.write("##")  # To give space between two lines
        st.write("""The ATL team of our school has participated in many competitions with this team 
        name, hence we have also named our team 'THE CRITICAL THINKERS’.
        """)
    with right_column:
    # st.write("""
    # chjhcjhd""")
        st.empty()
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Role of Team members in IRC 2023-24")
        st.write("##")  # To give space between two lines
        st.write("""Akhil, The Mechanical Worker, has designed our robot and has done 70% of the mechanical work. 
        \n Mayank, The Coder, has programmed the robot and helped Akhil in designing the robot. 
        \n Harsh, The Player, is quick at controlling the robot with the phone and remote control.
        \n Lakshay, The All Rounder, did 30% of the mechanical work and helped all the rest of his teammates.""")
    with right_column:
    # st.write("""
    # chjhcjhd""")
        st.empty()
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why did we participate in IRC?")
        st.write("##")  # To give space between two lines
        st.write("""Because IRC is Asia's biggest Robotics competition, we get to learn a lot from it and 
     with this we want to tell the world and our neighboring states that our school DAV
     PUBLIC SCHOOL THERMAL COLONY, PANIPAT, which is in the state of Haryana,
     also encourages and helps its students to progress in the field of 'Robotics'.
        """)
    with right_column:
    # st.write("""
    # chjhcjhd""")
        st.empty()
with st.container():
    st.write("---")
    st.header('Our Robot Design')
    st.write('##') # "##": This is a string that represents a Markdown header. In Markdown, "##" signifies a level 2 (h2) header
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Hanuman_ji)
        st.image(Arjun_ji)
        st.image(bhagvan_shiv)

    with text_column:
        # st.subheader("Jab Hanuman Ji Ne Apna Sina Chir Kar Dikhaya | Hanuman Movie Scene")
        # st.write("""
        # Jab Hanuman Ji Ne Apna Sina Chir Kar Dikhaya | 'Hanuman' Movie Scene
        # """)
        # st.write("[Watch Video...](https://youtu.be/2EOZjG8Xnv4)")
        # st.write('##')
        # st.write('##')
        # st.write('##')
        # st.write('##')
        # st.subheader("Arjun Status | Arjun Dialogue Status | Mahabharat Status Video | Whatsapp Status Video")
        # st.write("""
        #         Arjun Status | Arjun Dialogue Status | Mahabharat Status Video | Whatsapp Status Video
        #         """)
        # st.write("[Watch Video...](https://youtu.be/2bKPmU1ROiI)")
        # st.write('##')
        # st.write('##')
        # st.write('##')
        # st.subheader("Ajar Amar Shiv Shankar Song | Somnath Shiv Ji | Om Namah Shivay serial")
        # st.write("""
        #                 Ajar Amar Shiv Shankar Song | Somnath Shiv Ji | Om Namah Shivay serial
        #                 """)
        # st.write("[Watch Video...](https://youtu.be/IRULSFBzN5E)")
        # st.write('##')
        # st.write('##')
        # st.write('##')
        # st.write('##')
        # st.subheader("Hey Shiv Shankar Tripurari | Lord Shiva Song | Devotional Song | Peaceful Song")
        # st.write("""
        #                         Hey Shiv Shankar Tripurari | Lord Shiva Song | Devotional Song | Peaceful Song
        #                         """)
        # st.write("[Watch Video...](https://youtu.be/mtlFofkIMIY)")
        st.image(shivji_new)
        st.image(shivji_new1)
        st.empty()
with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")
    contact_form = """  
    <form action="https://formsubmit.co/davschoolthermalcolonypanipat@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """ # Html code

    left_column, right_column, third_column = st.columns((1.5,0.5,1))# ,gap="small"
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
         st.empty()
        # st.image(like_share.resize((450, 250)))
    with third_column:
        st.image(like_share.resize((400, 280)))
with st.container():
    # st.image('Like_share_subscribe.png', width=230)
    # st.image(like_share.resize((500, 300)))
    # st.markdown(
    #     f'<div style="display: flex; justify-content: center;"><img src="{like_share_new}" style="width: 50%; height: 50%;"></div>',
    #     unsafe_allow_html=True
    # )
    st.empty()



