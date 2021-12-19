import numpy as np
from random import randint
import pandas as pd

users=["손소독1", "손소독2", "손소독3", "손소독4"]
contents=["소독", "방역", "청결", "청소", "clear", "ssd"]

contents_vectors={
    "소독": [0.9, 0.34, 0.03, 0.12],
    "방역": [0.82, 0.6, 0.01, 0.01], 
    "청결": [0.56, 0.41, 0.09, 0.01],
    "청소": [0.85, 0.08, 0.55, 0.3], 
    "clear": [0.22, 0.5, 0.01, 0.9], 
    "ssd": [0.09, 0.74, 0.39, 0.6]
}

def make_demo_data():
    preference=[
        [1, 7, 8, 2, 4, 4],
        [7, 6, 5, 8, 5, 2], 
        [1, 1, 2, 7, 5, 1],
        [3, 6, 2, 7, 1, 7]
    ]

    def view_content_randomly(user_index):
        # user 의 선호 편향 점수를 가져와 0 ~ 20 범위 내의 숫자 중 무작위로 하나를 더하여 가장 큰 값을 가지는 index 를 반환
        additional_point=preference[user_index]
        rullet=list(randint(0, 20)+additional_point[content_index] for content_index in range(len(contents)))

        return np.argmax(rullet)
    
    view_history=[]

    for _ in range(1000):
        user_index=randint(0, len(users)-1)
        content_index=view_content_randomly(user_index)
        content_name=contents[content_index]
        view_history.append((user_index, users[user_index], content_index, content_name))

    df=pd.DataFrame(view_history, columns=["user_index", "user_name", "content_index", "content_name"])

    return df

def get_user_ratings(df_interaction):
    # user_index 와 content_index 가 같은 값인 행들의 개수를 저장
    df_user_view_count = df_interaction.groupby(["user_index","content_index"]).count()["content_name"]
    print(df_user_view_count)
    ratings=[]

    for index in range(len(users)):
        views=df_user_view_count[index].values

        result_view=sum(views)
        rating=views/result_view

        ratings.append(rating)

    return ratings

def init_user_vectors(user_num, feature_num):
    user_vectors=[]

    for i in range(user_num):
        user_v=np.random.normal(size=feature_num)
        user_vectors.append(user_v)
    
    return user_vectors

def update(user_vector, content_vector, loss, step_size=0.01):
    for index in range(len(user_vector)):
        yn=content_vector[index]
        
        # loss 와 step_size 에 비례하여 기존의 가중치를 조정
        dxn=(loss*step_size)*yn

        user_vector[index]+=dxn

if __name__=='__main__':
    df=make_demo_data()

    user_vectors=init_user_vectors(5, 4)
    content_vector_list=list(contents_vectors[i] for i in contents_vectors)
    ratings=get_user_ratings(df)

    def batch():
        loss_result=0

        for user_index in range(len(users)):
            for cindex, cv in enumerate(contents_vectors):
                rating_real=ratings[user_index][cindex]
                cv=contents_vectors[cv]
                v=np.dot(user_vectors[user_index], cv)
                loss=rating_real-v

                update(user_vectors[user_index], cv, loss)

            loss_result+=loss
        
        return loss_result
    
    def train():
        i=0
        loss_history=[]

        while i<1000:
            loss_result=batch()

            if i%10==0:
                print(f"{i} batch - loss : {loss_result}")

            i+=1
            loss_history.append(loss_result)
        
        return loss_history
    
    history=train()
    donald_vector=user_vectors[0]
    print(donald_vector)