import pandas as pnd
import numpy

data = pnd.read_csv("D:\IF 2020-2021\SMT 5\Pengantar AI\MEET 9\Diabetes.csv")

def subset_divide(data): #bagi subset sesuai ketentuan soal
    train_set1 = data[:614]
    test_set1 = data[614:]

    train_temp1 = data.loc[:461]
    train_temp2 = data.loc[615:]
    train_set2 = pnd.concat([train_temp1, train_temp2])
    test_set2 = data[461:614]

    train_temp1 = data.loc[:307]
    train_temp2 = data.loc[462:]
    train_set3 = pnd.concat([train_temp1, train_temp2])
    test_set3 = data[307:462]

    train_temp1 = data.loc[:154]
    train_temp2 = data.loc[308:]
    train_set4 = pnd.concat([train_temp1, train_temp2])
    test_set4 = data[154:308]

    train_set5 = data[155:768]
    test_set5 = data[:155]

    data_train = [train_set1, train_set2, train_set3, train_set4, train_set5]
    data_test = [test_set1, test_set2, test_set3, test_set4, test_set5]
    
    return data_train, data_test

def distance_count(row1, row2): #count eucledian distance
    distance = 0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return distance**(1/2)

def preprocess(dataset):#prapemrosesan data menggunakan rescaling data
    copy_data = dataset.copy(deep = True)
    copy_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = copy_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,numpy.NaN)
    copy_data['Glucose'].fillna(copy_data['Glucose'].mean(), inplace = True)
    copy_data['BloodPressure'].fillna(copy_data['BloodPressure'].mean(), inplace = True)
    copy_data['SkinThickness'].fillna(copy_data['SkinThickness'].median(), inplace = True)
    copy_data['Insulin'].fillna(copy_data['Insulin'].median(), inplace = True)
    copy_data['BMI'].fillna(copy_data['BMI'].median(), inplace = True)
    
    #scaling data csv soal
    for column in copy_data.columns[:-1]:
        copy_data[column] = (copy_data[column] - copy_data[column].mean()) / copy_data[column].std()
    
    train_scale, test_scale = subset_divide(copy_data)
    
    return train_scale, test_scale

def knn_classify(data_train, data_test, k):
    neighbors_distance = []
    prediction_res = []
    
    for h in range(len(data_test)):
        for i in range(len(data_train)):
            distance = distance_count(data_test.iloc[h], data_train.iloc[i])
            neighbors_distance.append([distance, data_train.index[i]])
            
        sorted_distance = sorted(neighbors_distance)
        
        data_k = sorted_distance[:k]
        
        for j in range(len(data_k)):
            result = data_train.loc[data_k[j][1]][-1]
            temp = data_k[j]
            temp.append(result)
        
        label_1 = 0
        prediction = 0
        
        for l in range(len(data_k)):
            if (data_k[l][2] == 1):
                label_1 += 1
                
        if (label_1 > (len(data_k)/2)):
            prediction = 1
        
        prediction_res.append([data_test.index[h], prediction])
    
    return prediction_res

def optimal_k(arr_accuracy):#find best K that contains the best accuracy value
    optimal = sorted(arr_accuracy, key = lambda x: x[1], reverse = True)
    return optimal[0]

def avg_accuracy(arr_accuracy): #count average of accuracy, scale is from 0 to 1
    temp = 0
    for data in arr_accuracy:
        temp += data
    return(temp/len(arr_accuracy))


training, testing = preprocess(data)
best_accuracy = []

for i in range(len(testing)):
    accuracy = []
    print('Amount of data on subset ',i+1,' = ',len(testing[i]))
    k = 1
    while k < 30:
        precision = 0
        prediction = knn_classify(training[i], testing[i], k)
        for m in range(len(prediction)):
            if (prediction[m][1] == testing[i].iloc[[m][0]][-1]):
                precision += 1
        print('K-',k,' correct predictions = ',precision)
        accuracy.append([k, (precision / len(testing[i]))])
        k += 4
    best_k = optimal_k(accuracy)
    print('best K point = ',best_k[0],' with an accuracy of ', best_k[1])
    best_accuracy.append(best_k[1])
average_accu = avg_accuracy(best_accuracy)
print('Average accuracy of best K point from 5 fold cross validation is ', average_accu)