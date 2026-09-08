/* SPDX-License-Identifier: GPL-2.0-or-later */
package org.libsdl.app;

import android.bluetooth.BluetoothGatt;
import android.bluetooth.BluetoothGattCharacteristic;
import android.bluetooth.BluetoothGattDescriptor;

/** A permission can be revoked between SDL's initial check and a GATT callback. */
final class BluetoothGattAccess {
    private BluetoothGattAccess() {}

    static boolean read(BluetoothGatt gatt, BluetoothGattCharacteristic value) {
        if (gatt == null) return false;
        try { return gatt.readCharacteristic(value); }
        catch (SecurityException denied) { return false; }
    }

    static boolean write(BluetoothGatt gatt, BluetoothGattCharacteristic value) {
        if (gatt == null) return false;
        try { return gatt.writeCharacteristic(value); }
        catch (SecurityException denied) { return false; }
    }

    static boolean notify(BluetoothGatt gatt, BluetoothGattCharacteristic value, boolean enabled) {
        if (gatt == null) return false;
        try { return gatt.setCharacteristicNotification(value, enabled); }
        catch (SecurityException denied) { return false; }
    }

    static boolean descriptor(BluetoothGatt gatt, BluetoothGattDescriptor value) {
        if (gatt == null) return false;
        try { return gatt.writeDescriptor(value); }
        catch (SecurityException denied) { return false; }
    }

    static boolean discover(BluetoothGatt gatt) {
        if (gatt == null) return false;
        try { return gatt.discoverServices(); }
        catch (SecurityException denied) { return false; }
    }

    static void disconnect(BluetoothGatt gatt) {
        if (gatt == null) return;
        try { gatt.disconnect(); }
        catch (SecurityException denied) { /* No permission to disconnect. */ }
    }

    static void close(BluetoothGatt gatt) {
        if (gatt == null) return;
        try { gatt.close(); }
        catch (SecurityException denied) { /* No permission to close. */ }
    }
}
