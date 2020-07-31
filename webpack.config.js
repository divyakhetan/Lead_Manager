module.exports = {
    module:{
        rules:[
            {
                //want for any js file and exclude for node module
                test: /\.js$/,
                exclude: /node_modules/,
                use:{
                    loader: "babel-loader"
                }
            }
        ]
    }
}