/***************************************************************************
    qgshiddenwidgetfactory.h
     --------------------------------------
    Date                 : 5.1.2014
    Copyright            : (C) 2014 Matthias Kuhn
    Email                : matthias at opengis dot ch
 ***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#ifndef QGSHIDDENWIDGETFACTORY_H
#define QGSHIDDENWIDGETFACTORY_H

#include "qgseditorwidgetfactory.h"
#include "qgis_gui.h"

SIP_NO_FILE

/**
 * \ingroup gui
 * \class QgsHiddenWidgetFactory
 * \brief Editor widget factory for hidden widgets.
 * \note not available in Python bindings
 */
class GUI_EXPORT QgsHiddenWidgetFactory : public QgsEditorWidgetFactory
{
  public:
    /**
     * Constructor for QgsHiddenWidgetFactory, where \a name is a human-readable
     * name for the factory.
     */
    QgsHiddenWidgetFactory( const QString &name );

    // QgsEditorWidgetFactory interface
  public:
    QgsEditorWidgetWrapper *create( QgsVectorLayer *vl, int fieldIdx, QWidget *editor, QWidget *parent ) const override;
    QgsEditorConfigWidget *configWidget( QgsVectorLayer *vl, int fieldIdx, QWidget *parent ) const override;
    bool isReadOnly() const override;
};

#endif // QGSHIDDENWIDGETFACTORY_H
