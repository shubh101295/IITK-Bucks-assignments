### Assignment3 solution

`python3 assignment3.py`

We have to convert data to bytes and sore them in <hash>.dat file (hash is the SHA-256 hash of input to the file)

##### Input Format: 

```
Enter number of inputs: <int>

## for each input 
Enter the transactionID: <64 bytes of hex characters>
Enter the index of output: <int>
Signature should a hex value containing even hex characters
Enter a signature: <string with even number of hex characters>

Enter number of outputs - <int>

## for each output
Enter the number of coins for output: <int>
Enter the relative path to publickey: <path_to_public_key>
```

##### Sample Input  
```
Enter number of inputs: 2

Input 1
Enter the transactionID: c90fcb62aac3469554903447e21e9fa0c8eb93c9353b830cf72a0b0682d02c54
Enter the index of output: 180561
Signature should a hex value containing even hex characters
Enter a signature: 6dea90fd730034dfcf2d8ea4cca799e0304a8c42431910150c3c5220e0b882464e95a9e7a4e3a049bdca13f1e87633388fcb22da196150a10cae5221cdb8475c6b59402df0cf7fff9f7399512e8519ba05c14ace7e107d3b9f64be070414178bcbe7585a9d293f938b220c9a32f913b534905b2a955b1d5f816033af4c08b311d183faf259d41751286519b6ea76a3d588cbe8b88b1b9bdf5cd28c43bafb8cf650ac7cc639da12a79d09a1c5826c92398f84b0785e95a55e500c9e7916f1803844fe5e9e5d37765b9e5854d575428ac63852d095b4108679daa04bcdebb90dd9663720a2c40c651356e64752167d29f15bd5e2c0b482fed7d46a069c0d33f082

Input 2
Enter the transactionID: 92a7c6d00b98e7824efe0a61bed2c9c7bbe7d787a15ff7dd8117bded3b74654d
Enter the index of output: 123
Signature should a hex value containing even hex characters
Enter a signature: 815f8a1c176d216a804f62be7ced9f82df1e82d5953d9b0757d71d6d7495a5305753c0f7353bd8754a9980446aac55eeef82a1ddd3791aac112a2be47f57c49b6799f5a624d97445dc6a416d2ccfd713564277ae69b9ba62d659c0e037296c0c1fa674b9a53c827a5857f7c982d2a41d9a6df16d6e2c39c8207381cb14c08204a1b18c7d17d3fe6e63e45fb3131821430942b51117476636a0ff1a3586e493efb44f8399a9d1e76d9c016278b492bd9d33e849a51c6139c99b16a6c91cfe1aac1567b6a26fe6fec7a5a11d0b218b4072f51a5c4b06d515580a1a8df99a65d7a35e2941393c400ac59dcb8f5f4d1e8c280cbc6a0917be8e9c58a43196ca495505

[<headers.Input object at 0x7ffb068dec18>, <headers.Input object at 0x7ffb068dee48>]
Enter number of outputs - 2

Enter the number of coins for output: 887766
Enter the relative path to publickey: ../../../012.pem

Enter the number of coins for output: 11223344
Enter the relative path to publickey: ../../../013.pem

Transaction Successfull
Saving data to 4363de44cf11799a8b2ae12074fc8edf82aa0ec698c5591498a5f286f59cf0f4.dat
```

