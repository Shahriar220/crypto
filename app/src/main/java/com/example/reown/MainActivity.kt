package com.example.reown

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.reown.ui.theme.ReownTheme
import com.reown.android.Core
import com.reown.android.relay.ConnectionType

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val connectionType = ConnectionType.AUTOMATIC
//        or ConnectionType.MANUAL
        val projectId = "f3465f16e9d43846b259b8444441dfbd" // Get Project ID at https://cloud.reown.com/
        val appMetaData = Core.Model.AppMetaData(
            name = "Kotlin.AppKit",
            description = "Kotlin AppKit Implementation",
            url = "kotlin.reown.com",
            icons = listOf("https://gblobscdn.gitbook.com/spaces%2F-LJJeCjcLrr53DcT1Ml7%2Favatar.png?alt=media"),
            redirect = "kotlin-modal-wc://request"
        )


//        CoreClient.initialize(projectId = projectId, connectionType = connectionType, application = this, metaData = appMetaData)
//
//        AppKit.initialize(
//            init = Modal.Params.Init(CoreClient),
//            onSuccess = {
//                // Callback will be called if initialization is successful
//            },
//            onError = { error ->
//                // Error will be thrown if there's an issue during initialization
//            }
//        )
        enableEdgeToEdge()
        setContent {
            ReownTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Greeting(
                        name = "Android",
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    ReownTheme {
        Greeting("Android")
    }
}