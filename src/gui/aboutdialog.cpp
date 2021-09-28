/*
 * Copyright (C) by Hannah von Reth <hannah.vonreth@owncloud.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
 * for more details.
 */
#include "aboutdialog.h"
#include "ui_aboutdialog.h"

#include "theme.h"
#include "guiutility.h"

#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QTcpSocket>


namespace OCC {

AboutDialog::AboutDialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::AboutDialog)
{
    setWindowFlags(windowFlags() & ~Qt::WindowContextHelpButtonHint);
    ui->setupUi(this);
    setWindowTitle(tr("About %1").arg(Theme::instance()->appNameGUI()));
    ui->aboutText->setText(Theme::instance()->about());
    // ui->icon->setPixmap(Theme::instance()->aboutIcon().pixmap(256));

// EducaMadrid
    if (hasConnectivity()) {
        QNetworkAccessManager *nam = new QNetworkAccessManager(this);
        connect(nam, &QNetworkAccessManager::finished, this, &AboutDialog::downloadFinished);
        const QUrl url = QUrl("https://avisos.educa.madrid.org/public/logos/footer/pt.png");
        QNetworkRequest request(url);
        nam->get(request);
    }else {
        ui->icon->setPixmap(Theme::instance()->aboutIcon().pixmap(256));
    }
// EducaMadrid
    ui->versionInfo->setText(Theme::instance()->aboutVersions(Theme::VersionFormat::RichText));

    connect(ui->versionInfo, &QTextBrowser::anchorClicked, this, &AboutDialog::openBrowserFromUrl);
    connect(ui->aboutText, &QLabel::linkActivated, this, &AboutDialog::openBrowser);
}
// EducaMadrid
bool AboutDialog::hasConnectivity() {
    QTcpSocket* sock = new QTcpSocket(this);
    sock->connectToHost("www.educa2.madrid.org", 80);
    bool connected = sock->waitForConnected(1000);//ms

    if (!connected)
    {
        sock->abort();
        return false;
    }
    sock->close();
    return true;
}

void AboutDialog::downloadFinished(QNetworkReply *reply) {
    QPixmap pm;
    pm.loadFromData(reply->readAll());
    ui->icon->setPixmap(pm);

    reply->deleteLater();
}
// EducaMadrid

AboutDialog::~AboutDialog()
{
    delete ui;
}

void AboutDialog::openBrowser(const QString &s)
{
    Utility::openBrowser(s, this);
}

void AboutDialog::openBrowserFromUrl(const QUrl &s)
{
    return openBrowser(s.toString());
}

}
