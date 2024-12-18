This repository is the official details of VoiceFLow- A completely voice automated curtain system made by Sourya Poudel.

Circuit Diagram:
![image](https://github.com/user-attachments/assets/3fa7ea61-bceb-41b5-81c4-5d797ac05eb0)

### Instructions for Setting Up Blynk and IFTTT for Motor Control

---

#### **1. Configure Blynk Dashboard**
1. **Login to Blynk Cloud**  
   - Navigate to [Blynk Cloud](https://blynk.cloud) and log in.  
   - Go to the **Template** page and click on **New Template**.  
     - **Template Name:** CONTROL DC MOTOR  
     - **Hardware:** ESP8266  
     - **Connection Type:** WiFi  

2. **Create Data Streams**  
   - Go to the **Data Stream** section and click on **New Data Stream**.  
   - Create the following virtual pins:  

      **Virtual Pin Configuration:**  
      | **Name**  | **Pin Number** | **Data Type** | **Max Value** |  
      |-----------|----------------|---------------|---------------|  
      | Motor1    | V1             | Double        | 255           |  
      | Motor2    | V2             | Double        | 255           |  

   - Click **Create** after each entry.  

   - Now, create additional variables to control motor direction using **Digital Pins**:  

      **Digital Pin Configuration:**  
      | **Name** | **Pin** | **GPIO Pin Correspondence** |  
      |----------|---------|----------------------------|  
      | M1F      | 5       | D1 (GPIO 5)               |  
      | M1R      | 4       | D2 (GPIO 4)               |  
      | M2F      | 0       | D3 (GPIO 0)               |  
      | M2R      | 2       | D4 (GPIO 2)               |  

3. **Web Dashboard Setup**  
   - Go to the **Web Dashboard** and add:  
     - **2 Slider Widgets**  
     - **4 Switch Widgets**  

   - Configure the widgets:  

      **Slider Settings:**  
      | **Slider** | **Title** | **Data Stream** |  
      |------------|-----------|-----------------|  
      | Slider 1   | Motor1    | Motor1 (V1)     |  
      | Slider 2   | Motor2    | Motor2 (V2)     |  

      **Switch Settings:**  
      | **Switch** | **Title** | **Data Stream** |  
      |------------|-----------|-----------------|  
      | 1          | M1F       | M1F (5)         |  
      | 2          | M1R       | M1R (4)         |  
      | 3          | M2F       | M2F (0)         |  
      | 4          | M2R       | M2R (2)         |  

   - Click **Save** when all configurations are complete.  

4. **Add Device**  
   - Click the **Search Button** and select **New Device**.  
   - From the template, select **CONTROL DC MOTOR**.  
   - Copy the generated **auth token** for later use.

---

#### **2. Upload the Code**
- Use the copied **auth token** in your program code.  
- **Optional Setup for Visual Studio Code (VSC):** Follow this [setup guide](https://www.youtube.com/watch?v=tc3Qnf79Ny8).  

---

#### **3. Configure Blynk Mobile App**
1. Open the **Blynk Application** on your mobile device.  
2. Locate the template you created.  
3. Add:  
   - **2 Sliders** and configure as done in the Web Dashboard.  
   - **4 Switches** and configure their corresponding data streams.  
4. Save the configuration.  

Now, your **ESP8266** control from the mobile app is ready.

---

#### **4. Enable Voice Control with IFTTT** [Free Alternative: Use the Python Code attached with the webhook url made as mentioned below]
1. **Login to IFTTT**  
   - Navigate to [IFTTT](https://ifttt.com).  
   - Go to **Create** to make a new applet.  

2. **Create Applet**  
   - **Trigger:**  
     - Select **Google Assistant v2**.  
     - Set a trigger phrase (e.g., "Open/Close Curtains").  
   - **Action:**  
     - Select **Webhooks**.  
     - Add a URL in this format:  

       ```  
       https://<region>.blynk.cloud/external/api/update?token=<auth_token>&pin=<virtual_pin>&value=<state>  
       ```  

       Example:  
       - **Region:** `blr1`  
       - **Server Address:** `blr.blynk.cloud`  
       - **Virtual Pin:** Use the corresponding pins for the motor controls.  
       - **Value:** `1` for "open" and `2` for "close".  

     - Paste the URL in the Webhooks configuration page.  
     - Press **Create Action**.  

3. **Link IFTTT to Google Assistant**  
   - Open the **Google App** on your phone.  
   - Navigate to **Settings > Google Assistant > Devices**.  
   - Select **Add a Device** > **Link a Device**.  
   - Search for **IFTTT** and add it.  

---

### You're all set!  
You can now control the motors via the Blynk Web and Mobile Dashboards or through voice commands using Google Assistant and IFTTT. 
