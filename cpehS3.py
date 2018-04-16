import boto.s3.key
import boto.s3.connection
import os

print('''
    ***********************************************************************
    *                                                                     *
    *                                                                     *
    *               ~   S3 Client Tool ~                                  *   
    *       !   Made By Saif Salah  !                                     *
    *                                                                     *
    *         [#] Please Follow Steps [#]                                 *
    *                                                                     *                                                                 
    ***********************************************************************
    ##########################################################################
    * [#] Step 1 Add => S3_ACCESS_KEY                                        *
    * [#] Step 2 Add => S3_SECRET_KEY                                        *
    * [#] Step 3 Add => End Point                                            *
    * [#] Step 4 Add Port => [ default is set 80 ]                           *    
    * [#] Step 5 Add SSL Secure  [ True ] if Available [ False is Default]   *
    * ##########################################################################
    
''')

def s3Controller():


    S3_ACCESS_KEY =  str(input('S3_ACCESS_KEY :'))

    S3_SECRET_KEY = str(input('S3_SECRET_KEY :'))

    endpoint = str(input('End Point :'))

    if(str(S3_ACCESS_KEY) != "" and str(S3_SECRET_KEY) != "" and str(endpoint) != ""):

        conn = boto.connect_s3(
            aws_access_key_id=S3_ACCESS_KEY,
            aws_secret_access_key=S3_SECRET_KEY,
            host=endpoint,
            is_secure=False,  # uncomment if you are not using ssl
            calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        )

        print("Well Well, S3 Connection Settings Successfully ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++ \n ")

        print('''
            [*] - Press 1 to upload object to Bucket
            [*] - Press 2 to  Get Objects Bucket Content
            [*] - Press 3 to Get Bucket List
        ''')

        Choose = int(input('Choose Option :) '))

        if(Choose == 1):

            print("Welcome to upload object Operation ")

            print("+++++++++++++++++++++++++++++++++++++++++++++++++ \n ")

            try:

                BUCKET = str(input("Bucket Name : "))

                filepath = str(input("File Path [ex /var/www/html/blablalba.mp4]: "))

                bucket = conn.lookup(BUCKET)

                key = boto.s3.key.Key(bucket)

                key.name = str(input("Please Enter Key Name with file extension if file have [ex : blablalba.mp4] "))

                key.set_contents_from_filename(filepath)

            except ValueError as e:
                print(e)
        elif(Choose == 2):

            print("Welcome to Get Objects Bucket Content Operation ")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++ \n ")

            bucket = str(input("Please Write Bucket Name: "))

            File = open("res.txt", 'w')
            for buckets in conn.get_bucket(bucket).list():

                File.write(buckets.name)

            File.close()
            path = os.getcwd()
            print("Please Check Your File on", path + "/" + File.name)


        elif(Choose == 3):

            print("Welcome to Get Bucket List  Operation ")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++ \n ")

            for buckets in conn.get_all_buckets():
                print(buckets.name)

        else:
            print("Please Check Your Input Must be Int")



    else:

        print("Sorry: check S3_ACCESS_KEY or S3_SECRET_KEY endpoint maybe empty")

s3Controller()
