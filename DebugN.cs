using UnityEngine;
using System.Collections;

public class DebugN : MonoBehaviour {
    private static DebugN instance; 

    private const string HOST_URL = "http://YOUR_IP_ADDRESS:YOUR_PORT";
 
    private void Initialize()
    {
        instance = this;
    }

    public static void Log(string message)
    {
        string data = string.Format("[LOG]:{1}", header, message);
        instance.StartCoroutine(instance.Request(HOST_URL, data));
    }

    private IEnumerator Request(string url, string data)
    {
        WWWForm form = new WWWForm();
        form.AddField("data", data);
        WWW hs_get = new WWW(url, form);
        yield return hs_get;
 
        if (hs_get.error != null)
            Debug.Log("There was an error: " + hs_get.error + " when sending \""+data+"\"");
        else
            Debug.Log("@" + data);
    }
}
