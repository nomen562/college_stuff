package com.codewithmosh;
class Browser {
    public void navigate(String address) {
        String ip = findIpAddress(address, true);
        String html = sendHttpRequest(ip);
    }

    private String sendHttpRequest(String ip) {
        return "<html></html>";
    }

    private String findIpAddress(String address, boolean cache) {
        return "127.0.0.1";
    }
}