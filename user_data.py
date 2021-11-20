users=["손소독1", "손소독2", "손소독3", "손소독4"]
contents=["소독", "방역", "청결", "세척", "살균", "청소", "clear", "무취", "세탁", "ssd"]

# 행은 user를 의미, 숫자는 content를 의미( 컴퓨터가 이해할 있게 숫자를 가진 행렬로 변환한 것 ) 
view_history=[
    [1,1,1,1,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,1],
]

# user를 통해 user id를 가지고 올 수 있어야 하고 그 반대의 경우도 가능해야 한다.
user_to_index={x: index for index, x, in enumerate(users)}
index_to_users={index: x for index, x in enumerate(users)}

content_to_index={x: index for index, x in enumerate(contents)}
index_to_content={index: x for index, x in enumerate(contents)}

# 이진법으로 표현된 데이터를 content의 이름이 담긴 데이터로 변환하는 함수
def decode_matrix(matrix):
    result=[]

    # view_history는 이중 배열이기에 1번째 루프는 행을 의미
    for user_view_history in matrix:
        user_view_history_decoded=[]

        # enumerate는 index와 value를 동시에 받을 때 사용
        for index, value in enumerate(user_view_history):
            # content에 참가했을 때 content 이름을 가져온다.
            if value==1:
                content_name=index_to_content[index]
                user_view_history_decoded.append(content_name)
            
        result.append(user_view_history_decoded)
    
    return result

if __name__=='__main__':
    matrix_decoded=decode_matrix(view_history)

    for user_view in matrix_decoded:
        print(user_view)